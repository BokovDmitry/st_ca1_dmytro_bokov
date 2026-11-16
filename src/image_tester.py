import numpy as np
import cv2
import requests
from PIL import Image

from src.preprocessor import preprocessing
from src.loaders.class_names import CLASS_NAMES

HEADERS = {'User-Agent': 'smart-tech-ca1-image-tester/1.0'}


def test_cifar10_set(model):
    print("CIFAR-10")
    url_automobile = "https://thumb.wikimedia.org/wikipedia/commons/thumb/9/94/Chevrolet_car_in_Quebec_city.jpg/500px-Chevrolet_car_in_Quebec_city.jpg"
    url_bird = "https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d8/Kadalundi_Bird_Sanctuary_Ardea_alba_09138.jpg/500px-Kadalundi_Bird_Sanctuary_Ardea_alba_09138.jpg"
    url_cat = "https://thumb.wikimedia.org/wikipedia/commons/thumb/2/2a/Cat_in_Efremov%2C_Russia1.jpg/500px-Cat_in_Efremov%2C_Russia1.jpg"
    url_deer = "https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f1/Red_Deer_Poing.JPG/500px-Red_Deer_Poing.JPG"
    url_horse = "https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c6/Horse_in_Kh%C3%B6vsg%C3%B6l.jpg/500px-Horse_in_Kh%C3%B6vsg%C3%B6l.jpg"
    test_model_with_image(model, url_automobile)
    test_model_with_image(model, url_bird)
    test_model_with_image(model, url_cat)
    test_model_with_image(model, url_deer)
    test_model_with_image(model, url_horse)


def test_cifar100_set(model):
    print("CIFAR-100")
    url_fox = "https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f4/Red_Fox_2025_10_07.jpg/500px-Red_Fox_2025_10_07.jpg"
    url_rabbit = "https://thumb.wikimedia.org/wikipedia/commons/thumb/8/8c/Rabbit_%28Oryctolagus_cuniculus%29_Skomer.jpg/500px-Rabbit_%28Oryctolagus_cuniculus%29_Skomer.jpg"
    url_squirrel = "https://thumb.wikimedia.org/wikipedia/commons/thumb/0/07/Grey_squirrel_%28Sciurus_carolinensis%29_02.jpg/500px-Grey_squirrel_%28Sciurus_carolinensis%29_02.jpg"
    url_bus = "https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ac/2024_EV_Motors_Japan_F8_series2-City_Bus_10.5m_Hiroshima_Bus.jpg/500px-2024_EV_Motors_Japan_F8_series2-City_Bus_10.5m_Hiroshima_Bus.jpg"
    url_tractor = "https://thumb.wikimedia.org/wikipedia/commons/thumb/2/28/T-25_tractor_2026_G1.jpg/500px-T-25_tractor_2026_G1.jpg"
    test_model_with_image(model, url_fox)
    test_model_with_image(model, url_rabbit)
    test_model_with_image(model, url_squirrel)
    test_model_with_image(model, url_bus)
    test_model_with_image(model, url_tractor)


def test_mixed_set(model):
    print("COMBINED")
    url_truck = "https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3e/Bakersfield%2C_%28CA%29_Truck_Kenworth_at_Flying_J_Travel_%285%29.jpg/500px-Bakersfield%2C_%28CA%29_Truck_Kenworth_at_Flying_J_Travel_%285%29.jpg"
    url_dog = "https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9d/Samoyed_dog_two_year_old_female_dllu.jpg/500px-Samoyed_dog_two_year_old_female_dllu.jpg"
    url_cat = "https://thumb.wikimedia.org/wikipedia/commons/thumb/3/37/Ginger_Kitten.jpg/500px-Ginger_Kitten.jpg"
    url_pickup_truck = "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b1/Chevy_Pickup_1939_5311560.jpg/500px-Chevy_Pickup_1939_5311560.jpg"
    url_cattle = "https://thumb.wikimedia.org/wikipedia/commons/thumb/8/8c/Cow_%28Fleckvieh_breed%29_Oeschinensee_Slaunger_2009-07-07.jpg/500px-Cow_%28Fleckvieh_breed%29_Oeschinensee_Slaunger_2009-07-07.jpg"
    url_trees = "https://thumb.wikimedia.org/wikipedia/commons/thumb/0/0e/Oak_tree_Sunol_Regional_Wilderness_California_2023_dllu.jpg/500px-Oak_tree_Sunol_Regional_Wilderness_California_2023_dllu.jpg"
    test_model_with_image(model, url_truck)
    test_model_with_image(model, url_dog)
    test_model_with_image(model, url_cat)
    test_model_with_image(model, url_pickup_truck)
    test_model_with_image(model, url_cattle)
    test_model_with_image(model, url_trees)


def test_model_with_image(model, image_to_test):
    r = requests.get(image_to_test, stream=True, headers=HEADERS)
    img = Image.open(r.raw)
    img = np.asarray(img)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    img = img.reshape(1, 32, 32, 1)
    print("Predicted class: " + CLASS_NAMES[np.argmax(model.predict(img), axis=1)[0]])
