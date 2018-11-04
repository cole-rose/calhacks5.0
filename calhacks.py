from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
import json
app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'C:\\Users\\user\\deep\\test_imgs'
configure_uploads(app, photos)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        result = str(get_prediction(filename))
        score = result[result.index("score:") + 7 : result.index("}")]

        displayName = result[result.index("display_name:") + 15 :-4]

        output = "<h1><br>"
        output = output + "Confidence:  <span style='color:red'>" + score + "</span><br>"
        output = output + "Classification: <span style='color:blue'>" + displayName + "</span></h1>"
        print(output)
        # loaded_json = json.loads(yo)
        # for x in loaded_json:
        #   print("%s: %d" % (x, loaded_json[x]))
        return output
    return render_template('upload.html')


import sys

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2


# def get_prediction(filename, project_id = 'C:\\Users\\Andrew\\Desktop\\calhacksimagedetection-221406-ca5c07414512', model_id='ICN114405975124524301'):
#   prediction_client = automl_v1beta1.PredictionServiceClient()

#   name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
#   payload = {'image': {'image_bytes': content }}
#   params = {}
#   request = prediction_client.predict(name, payload, params)
#   return request  # waits till request is returned


#   cur_dir = sys.argv[1] if len(sys.argv) > 1 else '.'


# # if __name__ == '__main__':
# #   file_path = sys.argv[1]
# #   project_id = sys.argv[2]
# #   model_id = sys.argv[3]

#   with open('file_path', 'rb') as ff:
#     content = ff.read()

#   return get_prediction(filename)

# #python predict.py YOUR_LOCAL_IMAGE_FILE imagedetection-221406 ICN114405975124524301


import sys

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2


def get_prediction(content, project_id ="imagedetection-221406", model_id = "ICN4845375387551194916"):
  prediction_client = automl_v1beta1.PredictionServiceClient()
  with open(content, 'rb') as ff:
    content = ff.read()
  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

# if __name__ == '__main__':
#   file_path = sys.argv[1]
#   project_id = sys.argv[2]
#   model_id = sys.argv[3]

  # with open(content, 'rb') as ff:
  #   content = ff.read()

  # return get_prediction(name)

if __name__ == '__main__':
    app.run(debug=True)




