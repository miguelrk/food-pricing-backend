import pyrebase
import os

dirpathSecrets = os.getcwd() + "/firebase_secrets.json"

firebaseConfig = {
  "apiKey": "AIzaSyCCL8LNWfr2Ri2wSOV8rjlbxZ4S1SWRWco",
  "authDomain": "tum-food-app.firebaseapp.com",
  "databaseURL": "https://tum-food-app.firebaseio.com",
  #"projectId": "tum-food-app",
  "storageBucket": "tum-food-app.appspot.com",
  #"messagingSenderId": "811530983997",
  #"appId": "1:811530983997:web:12889ab162f54f3f1be854",
  #"measurementId": "G-ZTTXZQNQE8",
  "serviceAccount": dirpathSecrets
}

#not used
firestoreConfig = {
  "type": "service_account",
  "project_id": "tum-food-app",
  "private_key_id": "7e4acad9218cf160f6d6eab56b4d2e17fe9df57e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC2mei9Z7TFKzWf\nFGwjDu+cVTEoVM6LgGEpBLNl3HIKAGRhn00YAWFz41L/E60AmpctXGhAUKIv9/q+\nm2RrwHy6FOMlItI/Ve/zcGM6FTFNKDkDe8xlw6DHfCFLbDNAl8eP0owPawSpyq6F\nmOs/QX6t3KDGc3ndsrb/3KNq6MImL4w9NmpZKR1EdVTtfXEbwzNiUwDzstXfoRsY\nJbnBe+Jdeqh85tzFbBB9fb6Mg04DQHFqGf8of3PJrdiHgw+buFotDXbymAE9RYPT\nbd/frTOZhLUknT6ixw/HbHcx6Uyqz1igonIKoVgG6gsKTf3QV70B0NqxH5cw7+kP\nJuKGYrNpAgMBAAECggEAMaGRrfGDI9hDwdJWNg04OWC6dMDgRvCE+BYsALKzWF6U\n6ifXV4AAkfQmuegKLNDX6F9mgpyoCKu5PpeT6umtvRIyTwSw6sAb8SoJ/l6GQPd+\nz6CVhM9wYugtUIe/Qn4+oqvSn9oxsUjCuNNAlbfii7UdCfOXGxgZP2AkFsnfA2uR\nCM/ah7keMMkVIgQ62zFwbN7rgGgsZuzSlEtzKL+G9SIkosM2HNr/w+mh5KVFhHER\n2kBpwO5vdIVTMcj7rLlUKFp4fdPxD6iXDlTlZngAHGWtYAOmNLwBX0Hw+MiQ1/mN\nBt7tLLQHe+nF1FNK5jQxJRHh0OVHcYToFhRAjU/VlQKBgQDsx3bhaipFDVIxWr4J\nCC50GH/+tghhx8XisaLOy4UuzFeSGeg3uphvSSF2kSB5mMfutbvSotlGsKxfzGpZ\n+FfwDaW9UtY56Xs/KhbCjamDiGsJGEDEcHtXJp16022up9gAPcmfzWSf+wSyCNff\nnmaKRUiqk0rzLwPnV803KJJ1gwKBgQDFbJD+tt2IWqyTNbcwF+NkyVLPM/DkHimG\nBPUBwE4OSO7dWPOCMLy2aw2DfY+b7PD/SWWTPqpaS/hoQm4+A4lU/JpJTmhrBlUk\n9YKT8A1lA1IvJlg4Xo6a0V2MTcoxFP8tftQ4wbJVMy8XeFrz2XST4luCLl7yhaVy\nu+4PitHLowKBgC0zetdXbBBYlatEVmjk/fE9yBl46Kq592XqYVk28wrXCZSji3gw\nD++Wt2OqGtf7uZcxbFSur+nVymJTZK4eQbNa95vn12ugzd1mDIhBgO3SOhS3Y43c\npz8g6QlMmXCxLAQHx5jRHfeIdQIDvCo9U/freA7QJYu9GvKsCUoRXbw/AoGBAJve\n9q+Uc133sS9dBrAa/DcT2KStbrC8u64LdeGXEkmm/aiXVVLh5ezkorvBQ8QpE7GL\nIn5ZyKgYOR0f7ehaZHBMLAhatohhbJIMoLbqnbi2IYoGbTq8NT04tfJTbKLJ4Brs\neuQA0isAiVqvdKf4dVlZK0SiFebG6/SlOfTddnyfAoGBAJoLfeKfQGUUPDguiKc3\neJSdw3nDklKgrhVXmuP8eTb2gqepbQTa+SGj2d+iU2xNvrjoCuZyLWn4UsjyCNpf\nE+sbgtTvxsalj4r+Lw8fRONRHV1Bj0gXz7aJVVWwGHosSXovNJv9ZoreKpgVw8FJ\nw2u0u9a1f43dgdwnbK5fy+za\n-----END PRIVATE KEY-----\n",
  "client_email": "tum-food-app-firestore@tum-food-app.iam.gserviceaccount.com",
  "client_id": "113945342687711934984",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tum-food-app-firestore%40tum-food-app.iam.gserviceaccount.com"
}


firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
storage = firebase.storage()
