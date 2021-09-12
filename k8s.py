from kubernetes import client, config

# 基于https证书(kubeconfig)
# config.load_kube_config(r'C:\Users\xbw12\PycharmProjects\k8s\config')

# 基于Token认证(ServiceAccount)
configuration = client.Configuration()
configuration.host = "https://192.168.100.10:6443"
configuration.ssl_ca_cert = r"C:\Users\xbw12\PycharmProjects\k8s\ca.crt"
configuration.verify_ssl = True
token = "eyJhbGciOiJSUzI1NiIsImtpZCI6InNvOV9xV25NREMtb2tlcWVSRU5tNklaYUduUHotSWsxZnpINlBHQ1dfSjgifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkYXNoYm9hcmQtYWRtaW4tdG9rZW4tbms3dGwiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGFzaGJvYXJkLWFkbWluIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiY2ZmMTU0OGItZjFhZS00NTE2LWE0NmEtZjVkZDM3YWY2YmJmIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmRhc2hib2FyZC1hZG1pbiJ9.Uko6GNtDBontYDpCbU0PXX7Aq6_Nz1pVou99eTBk0ne7M1twesgBJ-wLdAezmmyWLOgiiheLn19PZUcvJJdV6bEMFSBIc9xSqdNZMKTDI6jPisPfBCfRETyKBEOxG4sIAvkEf2QZSnirnHGbFmikSuvXVVtTayH1a42wRiD-4ZdCX1O9QvRNSCs9Ml002GrCmBs58G5XApPbt2aRpdTWwChQx5Q5PAej0mWBSyzHalnn2plV9tF2ajUmp-NBjdMdHKHd2jPtLykm0AVoB-nSY323_u2nSzywgCiPODczvgGq1yocwOjSGNIZ1eZa5tOGH2pXMdoKGWkCQfHQhmz9jA"
configuration.api_key = {"authorization": "Bearer " + token}
client.Configuration.set_default(configuration)

apps_api = client.AppsV1Api()

# print(apps_api.list_namespaced_deployment(namespace="kube-system"))
# for info in apps_api.list_namespaced_deployment(namespace="default").items:
#     print(info.metadata.name)
for dp in apps_api.list_deployment_for_all_namespaces().items:
    print(dp.metadata.name)

# 创建deployment
namespace = "default"
name = "api-test"
# replicas = 1
# labels = {'a':'1', 'b':'2'}  # 不区分数据类型，都要加引号
# image = "nginx"
# body = client.V1Deployment(
#             api_version="apps/v1",
#             kind="Deployment",
#             metadata=client.V1ObjectMeta(name=name),
#             spec=client.V1DeploymentSpec(
#                 replicas=replicas,
#                 selector={'matchLabels': labels},
#                 template=client.V1PodTemplateSpec(
#                     metadata=client.V1ObjectMeta(labels=labels),
#                     spec=client.V1PodSpec(
#                         containers=[client.V1Container(
#                             name="web",
#                             image=image
#                         )]
#                     )
#                 ),
#             )
#         )
# try:
#     apps_api.create_namespaced_deployment(namespace=namespace, body=body)
# except Exception as e:
#     status = getattr(e, "status")
#     if status == 400:
#         print(e)
#         print("格式错误")
#     elif status == 403:
#         print("没权限")

# apps_api.delete_namespaced_deployment(namespace=namespace, name=name)
