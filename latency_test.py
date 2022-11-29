from application import application
import json
import time
import statistics

dummy_test = ["this is a dummy test", {"prediction":1,"text":"this is a dummy test"}]
latency_measurements = []

def test_predict_latency():
    for i in range(100):
        start = time.time()
        response = application.test_client().get(
            '/predict?text=' + dummy_test[0])
        res = json.loads(response.data.decode('utf-8'))
        stop = time.time()
        latency_measurements.append(stop-start)
    
    average_latency = statistics.mean(latency_measurements)
    
    # to print average latency in command line please run `pytest -rP`
    print(average_latency)

    assert(average_latency < 0.01)
