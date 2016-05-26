
from system.core.controller import *
from flask import url_for

key = 'AIzaSyAZ8ZZI5pB010-a960_c8TzSnurR98IR6k'
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
        activity=self.models['Place'].get_activities(plan_id)
        return self.load_view('day_plan.html', activity=activity, key=key, plan_id=plan_id)

    def final_plan(self,plan_id):
        if session['id']==None:
            return redirect('/')
        activity=self.models['Place'].get_activities(plan_id)
        return self.load_view('final_plan.html', activity=activity, key=key)

    def create(self):

        info = {
             "name" : request.form['form-first-name'],
             "email": request.form['form-email'],
             "password":request.form['form-password'],
             "pw_confirmation" : request.form['form-conf-password']
        }
        print "this is", info

        create_status = self.models['Place'].create_user(info)
        if create_status['status'] == True:
            session['id'] = create_status['user']['id']

            return redirect('/user_info')
        else:

            for message in create_status['errors']:
                flash(message, 'regis_errors')

            return redirect('/')

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
            return redirect('/')
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
        self.models['Place'].starting_location(info,session['plan_id'])
        url='/day_plan/'+str(session['plan_id'])
        return redirect(url)

    def meals(self):
        print "day_plan is going on"
        if request.form['meal_alt']:
            meal = request.form['meal_alt']
        else:
            meal = request.form['meal']

        infos={
            'type':'meal',
            'category':meal,
            'price':request.form['price'],
            'duration':request.form['duration_meal'],
            'plan_id':session['plan_id'],
            'city':session['city'],
            'location':session['address'],
            'radius':session['radius']
            }
        session['type']=infos['type']
        meal_choices=self.models['Place'].search_meal(infos)

        return self.load_view('partials/index.html', data=meal_choices)

    def activity(self):
        if not request.form['activity']=="-":
            activity = request.form['activity']
        elif not request.form['activity_alt']=="-":
            activity = request.form['activity_alt']
        else:
            activity = request.form['activity_alt_alt']

        activity_info={
            'type':'activity',
            'category':activity,
            'duration':request.form['duration_activity'],
            'plan_id':session['plan_id'],
            'city':session['city'],
            'location':session['address'],
            'radius':session['radius']
        }
        session['type']=activity_info['type']
        act=self.models['Place'].search_activity(activity_info)
        return self.load_view('partials/index.html', data=act)
    def addactivity(self,plan_id):
        activity = request.form['activity'].split("+")
        name=activity[0]
        address=activity[1]
        info = {
            'name': name,
            'address': address,
            'type': session['type'],
            'plan_id':session['plan_id']
        }
        self.models['Place'].add_activity(info)
        activity=self.models['Place'].get_activities(plan_id)
        return self.load_view('partials/activities.html', activity=activity)
    def delete(self, id, plan_id):
        info={'id':id}
        delete=self.models['Place'].delete_activity(info)
        url = '/day_plan/'+str(plan_id)
        return redirect(url)