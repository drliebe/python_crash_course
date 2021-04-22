def make_car(manufacturer, model, **model_info):
    """Creating a dictionary to describe a car. Must include 
    manufacturer and model, but additional key,value information can be
    added as well through model_info."""
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    for key, value in model_info.items():
        car_info[key] = value
    return car_info