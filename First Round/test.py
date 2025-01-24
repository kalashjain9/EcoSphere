# from tensorflow.keras.models import load_model

# # Load the .h5 model
# model = load_model('/Users/jalpajigu/Desktop/Jaimeen Bhagat/Hackathons/KnowCode2.0/KnowCode_JaiHind/new/fire_detection_model (1).h5')

# # Use the model
# predictions = model.predict('/Users/jalpajigu/Desktop/Jaimeen Bhagat/Hackathons/KnowCode2.0/KnowCode_JaiHind/new/Forest_Fire_BigData/fire_images/abc002.jpg')

import h5py

# Open the .h5 file
with h5py.File('/Users/jalpajigu/Desktop/Jaimeen Bhagat/Hackathons/KnowCode2.0/KnowCode_JaiHind/new/fire_detection_model (1).h5', 'r') as file:
    # Explore the contents
    for key in file.keys():
        print(key)
