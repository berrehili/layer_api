import uuid
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from provider.oauth2.models import Client
from layer_api.serializers import RegistrationSerializer
from models import UserInfos

class RegistrationView(APIView):
    permission_classes = ()

    def post(self, request):
        try:
            data = request.DATA
            serializer = RegistrationSerializer(data=data)

            if not serializer.is_valid():
                return Response(serializer.errors,\
                                status=status.HTTP_400_BAD_REQUEST)
            NewUser_data = serializer.data

            NewUser = User.objects.create(username=NewUser_data["username"],password=NewUser_data['password'],email=NewUser_data['email'])
            NewUser.set_password(NewUser_data['password'])
            NewUser.save()
            if NewUser.id:
                UserDetails = UserInfos.objects.create(user_id=int(NewUser.id),firstname=data["firstname"],lastname=data["lastname"], email=data["email"], phone_number=data["phone_number"],\
                     birthday=data["birthday"])
                UserDetails.save()

                if UserDetails.id:
                    # Create OAuth2 client
                    name = NewUser.username
                    client = Client(user=NewUser, name=name, url='' + name,\
                        client_id=uuid.uuid4().hex, client_secret='', client_type=1)
                    client.save()

                    if not client.id:
                        NewUser.delete()
                else:
                    NewUser.delete()


            return Response({"message":"User created successfully !", "user_id": client.id,"client_id":str(client.client_id)})

        except Exception as e:
                raise



