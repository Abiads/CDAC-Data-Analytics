"""
Concepts used in this example:
1. Coroutine: a generator that consumes values using send().
2. Yield as suspension point: execution pauses until data is sent in.
3. Producer-consumer pattern: values can be passed into a coroutine step by step.
4. Generator closing: close() stops the coroutine cleanly.
"""

import time


# A coroutine is a generator-based function that receives values.
def get_weather_report():
    try:
        print("Please get me latitude and longitude as tuple")
        geo_str = yield
        print(f"I received the data as a tuple: please verify : {geo_str}")
        print("Please get me the parameters to extract")
        geo_par = yield
        print(f"Parameter request is : {geo_par}")
        print("result format expected ")
        result_format = yield
        print(f"Job is done and result is ready in {result_format}")
        final_res = yield
    except GeneratorExit:
        print("Generator stopped from outside")


gen1 = get_weather_report()
next(gen1)  # prime the coroutine: start execution until first yield

gen1.send((1234.567, 34566.4433))
time.sleep(3)
gen1.send(("Wind Speed", "Humidity"))
time.sleep(3)
gen1.send(("xml", "json"))
gen1.close()



