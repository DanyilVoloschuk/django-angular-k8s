k8s_yaml('./k8s/postgres/deployment.yaml')

k8s_resource(
    'django',
    port_forwards='5432:5432',
    labels=['backend']
)

docker_build(
    'django-k8s-test-project',
    context='.',
    dockerfile='be_tour_of_heroes/Dockerfile',
    live_update=[
        sync('.be_tour_of_heroes/', '/app/be_tour_of_heroes'),
        run(
            'pip install -r requirements.txt',
            trigger=['be_tour_of_heroes/requirements.txt']
        )
    ]
)


k8s_yaml('./k8s/django/deployment.yaml')

k8s_resource(
    'django',
    port_forwards='8000:8000',
    labels=['backend']
)
