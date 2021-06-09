from django.shortcuts import render
import pickle

def home(request):
    return render(request, 'index.html')

def getPredictions(id, longitude, latitude, gps_height, quality_group, district_code, region_code, extraction_type, waterpoint_type):
    model = pickle.load(open('Compress_Model.sav', 'rb'))

    prediction = model.predict([
        [id, longitude, latitude, gps_height, quality_group, district_code, region_code, extraction_type, waterpoint_type]
    ])
    
    if prediction == 2:
        return 'non functional'
    elif prediction == 0:
        return 'functional'
    else:
        return 'functional needs repair'

def result(request):
    id = int(request.GET['id'])
    longitude = float(request.GET['longitude'])
    latitude = float(request.GET['latitude'])
    gps_height = float(request.GET['gps_height'])
    quality_group = int(request.GET['quality_group'])
    district_code = int(request.GET['district_code'])
    region_code = int(request.GET['region_code'])
    extraction_type = int(request.GET['extraction_type'])
    waterpoint_type = int(request.GET['waterpoint_type'])

    result = getPredictions(id, longitude, latitude, gps_height,
                            quality_group, district_code, region_code, extraction_type, waterpoint_type)

    return render(request, 'result.html', {'result': result})
