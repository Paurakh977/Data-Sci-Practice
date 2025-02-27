from icecream import ic
from datetime import datetime
# basic nested dict.
user = {
    'username': 'johndoe',
    'details': {
        'name': 'John Doe',
        'age': 30
    }
}

# to add some details
user['details']['email']="abc@gmail.com"
user['details']['age'] = 21
user['details'].update({"location":"KTM","Home":"rental"})
user['details'].update({'phones': ['123-456-7890']})
ic(user)  #ic| user: {'details': {'Home': 'rental',        
                #                'age': 21,
                #                'email': 'abc@gmail.com',
                #                'location': 'KTM',
                #                'name': 'John Doe',
                #                'phones': ['123-456-7890']},
            #                     'username': 'johndoe'}
            
# append phone numbers
user['details']['phones'].append("01-97322")

# merging of nested dict 

default_settings = {
    'notifications': {
        'email': True,
        'sms': False
    }
}
user_settings = {
    'notifications': {
        'sms': True,
        'subscriptions':False
    }
}
ic("initial",default_settings)

res=  default_settings | user_settings
# this updates only the exsiting and matching values
ic(res)

default_settings['notifications'].update(user_settings['notifications'])
# this updates subscriptions key too
ic(default_settings)

# Mini-task

fitness_tracker = {
    'users': [
        {
            'id': 'U123',
            'name': 'Alex Smith',
            'age': 28,
            'settings': {
                'units': 'metric',
                'notifications': True
            }
        },
        {
            'id': 'U456',
            'name': 'Priya Patel',
            'age': 34,
            'settings': {
                'units': 'imperial',
                'notifications': False
            }
        }
    ],
    'workouts': [
        {
            'user_id': 'U123',
            'date': '2025-02-25',
            'type': 'running',
            'distance_km': 5.5,
            'duration_min': 30,
            'calories': 350,
            'notes': ['Felt great']
        },
        {
            'user_id': 'U123',
            'date': '2025-02-25',
            'type': 'yoga',
            'distance_km': 0,
            'duration_min': 20,
            'calories': 100,
            'notes': ['Post-run stretch']
        },
        {
            'user_id': 'U123',
            'date': '2025-02-26',
            'type': 'strength',
            'exercises': [
                {'name': 'Push-ups', 'reps': 20},
                {'name': 'Squats', 'reps': 15}
            ],
            'duration_min': 45,
            'calories': 200
        },
        {
            'user_id': 'U456',
            'date': '2025-02-24',
            'type': 'cycling',
            'distance_km': 9.977908,  # 6.2 miles converted (1 mi = 1.60934 km)
            'duration_min': 35,
            'calories': 300,
            'notes': ['Rainy day']
        },
        {
            'user_id': 'U456',
            'date': '2025-02-26',
            'type': 'strength',
            'exercises': [
                {'name': 'Bench Press', 'reps': 10},
                {'name': 'Deadlifts', 'reps': 8}
            ],
            'duration_min': 50,
            'calories': 250
        },
        {
            'user_id': 'U456',
            'date': '2025-02-26',
            'type': 'walking',
            'distance_km': 3.21868,  # 2.0 miles converted
            'duration_min': 30,
            'calories': 120,
            'notes': ['Evening stroll']
        }
    ],
    'goals': [
        {
            'user_id': 'U123',
            'type': 'weekly',
            'metrics': {'distance_km': 20, 'calories': 1500},
            'achieved': False
        },
        {
            'user_id': 'U456',
            'type': 'weekly',
            'metrics': {'distance_km': 24.1401, 'calories': 1000},  # 15 miles converted
            'achieved': False
        },
        {
            'user_id': 'U123',
            'type': 'monthly',
            'metrics': {'distance_km': 80, 'calories': 6000},
            'achieved': True,
            'completed_on': '2025-02-28'
        },
        {
            'user_id': 'U456',
            'type': 'daily',
            'metrics': {'steps': 10000, 'calories': 2000},
            'achieved': True,
            'completed_on': '2025-02-26'
        },
        {
            'user_id': 'U789',
            'type': 'yearly',
            'metrics': {'distance_km': 300, 'calories': 25000},
            'achieved': True,
            'completed_on': '2025-12-31'
        },
        {
        'user_id': 'U123',
        'type': 'monthly',
        'metrics': {'distance_km': 70, 'calories': 6000},
        'achieved': True,
        'completed_on': '2025-02-31'
    },
    ],
    'app_info': {
        'version': '2.1.3',
        'last_updated': '2025-02-27',
        'active_users': 2
    }
}

# Task 1: Update User Settings
# Turn off notifications for Alex.

def update_settings(dict_to_update: dict, user: str , new_settings: dict)->bool:
    for items in dict_to_update['users']:
        if items['name']==user:
            items['settings'].update(new_settings)
            ic(items['name'], items['settings'])
            return True
    return False   
            
update_settings(fitness_tracker,"Alex Smith", {
                'units': 'metric',
                'notifications': False
            } )
# Task 2: Add a New Workout
# Add a new workout on '2025-02-27': cycling, 10 km, 40 minutes, 400 calories, with a note "Hilly route" for uid U123.

def add_workout(dict_to_update: dict,user_id:str, new_workout:dict)->bool:
    try:
        fitness_tracker['workouts'].append(new_workout)
        return True
    except:
        return False
    
add_workout(fitness_tracker,"U123",{
            'user_id': 'U123',
            'date': '2025-02-27',
            'type': 'cycling',
            'distance_km': 10,
            'duration_min': 40,
            'calories': 400,
            'notes': ['Hilly route']
        },)


# Task 3: Update Workout Data
# U456 wants to do pushpus  on 2025-02-26 instead of walking update accoridngly .

def update_exercise(dict_to_update: dict, user_id: str, new_props: dict, date: str, type_to_update: str) -> bool:
    return any(items.update(new_props) or True for items in dict_to_update['workouts'] if items.get('user_id') == user_id and items.get('date') == date and items.get('type') == type_to_update)


update_exercise(fitness_tracker,'U456', new_props={
            'type':"pushups",
            'distance_km': 0,  
            'duration_min': 30,
            'calories': 500,},date="2025-02-24",type_to_update="cycling")


def get_personal_info(user_id:str,data:dict =fitness_tracker)->dict|None:
    return next(item for item in data['users'] if item['id'] == user_id)


def get_calories_and_duration(user_id: str, till_date: str, data: dict = fitness_tracker) -> tuple[int, int]:
    return tuple(sum(values) for values in zip(*((item.get("calories", 0), item.get("duration_min", 0)) 
             for item in data['workouts'] if item['user_id'] == user_id 
             and datetime.strptime(item['date'], "%Y-%m-%d") <= datetime.strptime(till_date, "%Y-%m-%d"))))

def get_goals_description(user_id: str, data: dict = fitness_tracker) -> dict:

    return {'completed_goals': [
        {'metrics': goal['metrics'], 'completed_on': goal['completed_on']}
        for goal in data['goals']
        if goal['user_id'] == user_id and goal.get('achieved', False)
    ]} 

    
# Task 4: Give all the user descriptions and  give the total calories burned till the date also the goals description completed till the date

def get_details(user_id:str,till_date:str,data:dict = fitness_tracker):
    description_dict={}
    description_dict.update(get_personal_info(user_id=user_id))
    calories, duration = get_calories_and_duration(user_id,till_date)
    description_dict.update({"calories_burned": calories,"duration": duration})
    description_dict.update(get_goals_description(user_id=user_id))
    ic(description_dict)

    # print(f"user_name : {description_dict.get('name',"Not Found")}\n age : {description_dict.get("age","Not Found")}\n Exerceise Duration : {description_dict.get("duration","Not Found")}\n Calories Burned: {description_dict.get("calories_burned","Not Found")}\n goals compelted on :", *[goal_dict.get('completed_on',"No dates found") for goal_dict in description_dict.get("completed_goals",[])])
    # this is because * cannot be done in f sting so better alternative is
    print(f"user_name : {description_dict.get('name', 'Not Found')}\n"
      f"age : {description_dict.get('age', 'Not Found')}\n"
      f"Exercise Duration : {description_dict.get('duration', 'Not Found')}\n"
      f"Calories Burned: {description_dict.get('calories_burned', 'Not Found')}\n"
      f"goals completed on : {', '.join(goal_dict.get('completed_on', 'No dates found') for goal_dict in description_dict.get('completed_goals', []))}")



get_details('U123',"2025-02-25",fitness_tracker)