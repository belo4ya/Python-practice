<details>
<summary> 1. Базовые типы данных </summary>

   - Неизменяемые:
   ```int```, ```float```, ```complex```, ```str```, ```bytes```, ```None```, ```bool```, ```tuple```, ```frozenset```
   - Изменяемые:
   ```dict```, ```list```, ```set```
        
</details>

<details>
<summary> 2. Функциональное программирование </summary>
   
   - ```lambda```, ```zip```, ```map```, ```filter```, ```reduce``` (functools)

   ```python
numbers = range(10)
squared_evens = map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers))
list(squared_evens)   # [0, 4, 16, 36, 64]
   ```

   - Декораторы:
   
   ```python
from functools import wraps
    
def logger(filename):

    def decorator(func):

        @wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "w+") as f:
                f.write(str(result))
            return result

        return wrapped

    return decorator
   ```
    
</details>

<details>
<summary> 3. Генераторы, выражения-генераторы, иттераторы </summary>

   - Генератор - это функция содержащая ключевое слово ```yield```.
   Генераторы позволят осуществлять ленивые вычисления. Также является иттератором.
   
   ```python
def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b
   ```

   - Выражения-генераторы предназначены для компактного и удобного способа генерации коллекций элементов.
   
   ```python
iter_ = (i ** 2 if i % 2 == 0 else i for i in range(5))  # <generator object <genexpr> at 0x000002D0E5219660>
list_ = [i ** 2 for i in range(10) if i % 2 == 0]  # [0, 4, 16, 36, 64]
set_ = {i for i in range(0, 10, 2)}  # {0, 2, 4, 6, 8}
dict_ = {v: k for k, v in {'a': 1, 'b': 2, 'c': 3}.items()}  # {1: 'a', 2: 'b', 3: 'c'}
   ```
   
   - Итератор — это сущность порождаемая функцией iter, с помощью которой происходит итерирование итерируемого объекта. 
   Итерируемый объект — это что-то, что можно итерировать. Итератор не имеет индексов и может быть использован только один раз.
   
   ```python
# реализация с помощью генераторов

def infinity(step):
    i = 0
    while True:
        yield i
        i += step

iter_ = infinity(10)
next(iter_)  # 0
next(iter_)  # 10
next(iter_)  # 20
   ```

   ```python
# реализация с помощью переопределения магических методов класса

class Arrange:

    def __init__(self, start, stop, step):
        self.i = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.stop:
            raise StopIteration

        result = self.i
        self.i += self.step
        return result
   ```
   
</details>

<details>
<summary> 4.  </summary>

</details>

3. ООП:
    - Класс — это описание того, какими свойствами и поведением будет обладать объект. А объект — это экземпляр с собственным состоянием этих свойств.

    - абстракция:
        - Выделение главных, наиболее значимых характеристик предмета и отбрасывание второстепенных, незначительных.
    - наследование
        - Позволяет описать новый класс на основе существующего (родительского). Повторное использование кода.
    - полиморфизм
        - Возможность работать с несколькими типами так, будто это один и тот же тип. Прри этом 
        поведение объектов будет разным.
    - инкапсуляция
        - Ограничение доступа к данным и возможностям их изменения путем сокрытия их в классе. (в Python существует как договоренность)


3. Побитовые операции:
    - ```x | y``` (или)
    - ```x ^ y``` (исключающее или)
    - ```x & y``` (и)
    - ```x << y``` (битовый сдвиг влево)
    - ```x >> y``` (битовый сдвиг вправо)
    - ```~x``` (инверсия)

4. Вирутуальное окружение:
    - ```python -m venv "env"```



<details>
  <summary>Spoiler warning</summary>
  
  Spoiler text. Note that it's important to have a space after the summary tag. You should be able to write any markdown you want inside the `<details>` tag... just make sure you close `<details>` afterward.
  
  ``` javascript 
  console.log("I'm a code block!");
  ```
  




- List comprehension (Генераторы списков)

- KISS, DRY, SOLID, CRUD, REST, SOAP

