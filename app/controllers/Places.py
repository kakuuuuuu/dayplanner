
from system.core.controller import *
from flask import url_for

key = 'AIzaSyAZ8ZZI5pB010-a960_c8TzSnurR98IR6k'
key2='47521c561e87f14aedc9be6469d7968c'
class Places(Controller):
    def __init__(self, action):
        super(Places, self).__init__(action)

        self.load_model('Place')
        self.db = self._app.db
        if 'id' not in session:
            session['id']=None
        if 'name' not in session:
            session['name']=''
        if 'city' not in session:
            session['city']=''
        if 'address' not in session:
            session['address']=''
        if 'radius' not in session:
            session['radius']=''
        if 'plan_id' not in session:
            session['plan_id']=''
        if 'type' not in session:
            session['type']=''
    def home(self):
        if session['id']!=None:
            return redirect('/user_info')
        return self.load_view('dayplayhome.html')
    def index(self):
        if session['id']!=None:
            return redirect('/user_info')
        return self.load_view('index.html')

    def user_info(self):
        if session['id']==None:
            return redirect('/')
        trips=self.models['Place'].get_trips(session['id'])
        return self.load_view('user_info.html', trips=trips)

    def day_plan(self, plan_id):
        if session['id']==None:
            return redirect('/')
        user_id=self.models['Place'].check_plan(plan_id)
        if user_id == False:
            return redirect('/')
        else:
            if session['id']!=user_id[0]['users_id']:
                return redirect('/')
        start = self.models['Place'].get_activities(plan_id)
        if len(start)<1:
            self.models['Place'].delete_plan(plan_id)
            return redirect('/')
        city = start[0]['category']
        info={'location':city}
        weather_info=self.models['Place'].search_weather(info)
        temp=round((1.8*(weather_info['main']['temp']-273)+32))
        if temp<40:
           flash('Its too cold')
           img="/static/images/cold.png"
        elif temp>85:
           flash("Its too hot")
           img="/static/images/hot.png"
        else:
           flash('Awsome weather')
           img="/static/images/awsome.jpeg"
        description=weather_info['weather'][0]['description']
        rain="rain"
        if rain in description:
           flash('It might rain')
           img='/static/images/rain.jpg'
        activity=self.models['Place'].get_activities(plan_id)
        return self.load_view('day_plan.html', activity=activity, key=key, plan_id=plan_id, weather_info=weather_info, temp=temp, img=img)

    def final_plan(self,plan_id):
        if session['id']==None:
            return redirect('/')
        user_id=self.models['Place'].check_plan(plan_id)
        if user_id == False:
            return redirect('/')
        else:
            if session['id']!=user_id[0]['users_id']:
                return redirect('/')
        start = self.models['Place'].get_activities(plan_id)
        if len(start)<=0:
            self.models['Place'].delete_plan(plan_id)
            return redirect('/')
        city = start[0]['category']
        info={'location':city}
        weather_info=self.models['Place'].search_weather(info)
        temp=round((1.8*(weather_info['main']['temp']-273)+32))
        if temp<40:
           flash('Its too cold')
           img="/static/images/cold.png"
        elif temp>85:
           flash("Its too hot")
           img="/static/images/hot.png"
        else:
           flash('Awsome weather')
           img="/static/images/awsome.jpeg"
        description=weather_info['weather'][0]['description']
        rain="rain"
        if rain in description:
           flash('It might rain')
           img='/static/images/rain.jpg'
        activity=self.models['Place'].get_activities(plan_id)
        return self.load_view('final_plan.html', activity=activity, key=key, plan_id=plan_id,  weather_info=weather_info, temp=temp, img=img)

    def create(self):
        info = {
             "name" : request.form['form-first-name'],
             "email": request.form['form-email'],
             "password":request.form['form-password'],
             "pw_confirmation" : request.form['form-conf-password']
        }
        if info['name']<2:
            errors.append('Name must be longer than 2 characters')

        create_status = self.models['Place'].create_user(info)
        if create_status['status'] == True:
            session['id'] = create_status['user']['id']

            return redirect('/user_info')
        else:

            for message in create_status['errors']:
                flash(message, 'regis_errors')

            return redirect('/start')

    def login(self):

        info = {
            "email" : request.form['form-email'],
            "password" : request.form['form-password']
        }
        print "before calling create_status"
        create_status = self.models['Place'].login(info)

        if create_status['status'] == True:
            print "we are in create_status=True"
            session['id'] = create_status['user']['id']
            session['name'] = create_status['user']['name']
            print session['id']
            return redirect('/user_info')
        else:

            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/start')
    def logout(self):
        if 'id' in session:
            session['id']=None
        if 'name' in session:
            session['name']=''
        if 'city' in session:
            session['city']=''
        if 'address' in session:
            session['address']=''
        if 'radius' in session:
            session['radius']=''
        if 'plan_id' in session:
            session['plan_id']=''
        if 'type' in session:
            session['type']=''
        return redirect('/')
    def options(self):
        info={
        'main_location':request.form['location'],
        'start_time':request.form['start_time'],
        'end_time':request.form['end_time'],
        'start_location':request.form['start_location'],
        'users_id':session['id'],
        'transportation':request.form['transportation']
        }
        print request.form['transportation']
        session['radius']=request.form['transportation']
        print session['radius']
        session['city']=request.form['location']
        session['address']=request.form['start_location']
        session['plan_id']=self.models['Place'].insert_planning_data(info)
        check = self.models['Place'].starting_location(info,session['plan_id'])
        if check['status']==False:
            flash(check['error'])
            self.models['Place'].delete_plan(session['plan_id'])
            return redirect('/user_info')
        url='/day_plan/'+str(session['plan_id'])
        return redirect(url)

    def meals(self, plan_id):
        print "day_plan is going on"
        if request.form['meal'] == '-':
            meal = request.form['meal_alt']
        else:
            meal = request.form['meal']
        start = self.models['Place'].get_activities(plan_id)[0]
        infos={
            'type':'Food',
            'category':meal,
            'price':request.form['price'],
            'duration':request.form['duration_meal'],
            'plan_id':plan_id,
            'city':start['category'],
            'location':start['address'],
            'radius':session['radius']
            }
        session['type']=infos['type']
        meal_choices=self.models['Place'].search_meal(infos)

        return self.load_view('partials/index.html', data=meal_choices, plan_id=plan_id, start=start)

    def activity(self, plan_id):
        if not request.form['activity']=="-":
            activity = request.form['activity']
        elif not request.form['activity_alt']=="-":
            activity = request.form['activity_alt']
        else:
            activity = request.form['activity_alt_alt']
        start = self.models['Place'].get_activities(plan_id)[0]
        activity_info={
            'type':'Activity',
            'category':activity,
            'duration':request.form['duration_activity'],
            'plan_id':plan_id,
            'city':start['category'],
            'location':start['address'],
            'radius':session['radius']
        }
        session['type']=activity_info['type']
        act=self.models['Place'].search_activity(activity_info)
        return self.load_view('partials/index.html', data=act, plan_id=plan_id, start=start)
    def addactivity(self,plan_id):
        activity = request.form['activity'].split("+")
        name=activity[0]
        address=activity[1]
        info = {
            'name': name,
            'address': address,
            'type': session['type'],
            'plan_id':plan_id
        }
        self.models['Place'].add_activity(info)
        activity=self.models['Place'].get_activities(plan_id)
        return self.load_view('partials/activities.html', activity=activity)
    def delete(self, id, plan_id):
        info={'id':id}
        delete=self.models['Place'].delete_activity(info)
        url = '/day_plan/'+str(plan_id)
        return redirect(url)
    def deleteplan(self, plan_id):
        self.models['Place'].delete_plan(plan_id)
        return redirect('/user_info')
