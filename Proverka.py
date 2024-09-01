friends = ['Alice', 'Bob', 'Charlie', 'Megan', 'Mark', 'Michael']
filtered_friends = list(filter(lambda x: x.startswith('M'), friends)) # Используем filter с лямбда-функцией для выбора имен, начинающихся с "M"
print(filtered_friends)
def test_filter():
    assert list(filter(lambda x: x.startswith('M'), friends)) == ['Megan', 'Mark', 'Michael']
