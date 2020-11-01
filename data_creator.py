import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

names = [fake.name() for i in range(100)]
cities = [fake.city() for i in range(100)]
ages = np.random.random_integers(0, 100, size=100)

df = pd.DataFrame({"name": names, "age": ages, "city": cities})

df.to_feather("_data/test_data.feather")
