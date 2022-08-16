from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import requests
# Create your views here.
openstack_hostIP = "172.30.1.57"

def token():
    # Admin으로 Token 발급 Body
    token_payload = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": "admin",
                        "domain": {
                            "name": "Default"
                        },
                        "password": "0000"
                    }
                }
            }
        }
    }

    # Openstack keystone token 발급
    auth_res = requests.post("http://" + openstack_hostIP + "/identity/v3/auth/tokens",
        headers = {'content-type' : 'application/json'},
        data = json.dumps(token_payload))

    #발급받은 token 출력
    admin_token = auth_res.headers["X-Subject-Token"]
    #print("token : \n",admin_token)
    return admin_token

class openstack_create(APIView):    #하나로 합치기
    def post(self, request):
        admin_token = token()
        flavor_id = "d1"
        instance_name = "django_test2"#input("생성할 인스턴스 이름 입력: ")
        # 특정 (shared) 네트워크 참조
        network_uuid = requests.get("http://" + openstack_hostIP + ":9696/v2.0/networks?name=public",
            headers = {'X-Auth-Token' : admin_token}
            ).json()["networks"][0]["id"]
        #print(network_uuid)
        # print()
        # print("network uuid : "+network_uuid)
        # print()

        # 특정 img id 참조
        # img_uuid = requests.get("http://" + openstack_hostIP + "/image/v2/images?name=ubuntu",  #해당 이미지는 내 서버에 없으므로 수정할 것
        #     headers = {'X-Auth-Token' : admin_token}
        #     ).json()["images"][0]["id"]

        
        # flavor_reference= input("flavor ref id 입력: ")
        openstack_instance_payload = {
            "server" : {
                "name" : instance_name,
                "imageRef" : "d7626315-8f03-4fd6-9938-d9d208440136",#img_uuid,
                "flavorRef" : flavor_id,
                "networks" : [{
                    "uuid" : network_uuid
                }] 
            }
        }
        #인스턴스 생성 요청
        user_res = requests.post("http://" + openstack_hostIP + "/compute/v2.1/servers",
            headers = {'X-Auth-Token' : admin_token},
            data = json.dumps(openstack_instance_payload))
        # print(user_res.json())

        return Response(user_res.json())

class openstack_list(APIView):
    def get(self, request): #임시로 인스턴스 정보 get 해오는 것 test
        admin_token = token()
        user_res = requests.get("http://" + openstack_hostIP + "/compute/v2.1/servers/39f9010d-f114-4d8a-89b5-abdcfc06608c",
            headers = {'X-Auth-Token' : admin_token})
        
        return Response(user_res.json())