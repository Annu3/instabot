from clarifai.rest import ClarifaiApp
app=ClarifaiApp(api_key='b40b2d24a82b4cab89ec2ec4af04874a')
model=app.models.get('weddings-v1.0')
response=model.predict_by_url('http://www.fennes.co.uk/wp-content/uploads/2014/10/fennes_wedding.jpg')
print response