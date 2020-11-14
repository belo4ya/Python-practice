<details>
<summary> 1. Базовые типы данных </summary>

   - неизменяемые:
   ```int```, ```float```, ```complex```, ```str```, ```bytes```, ```None```, ```bool```, ```tuple```, ```frozenset```
   - изменяемые:
   ```dict```, ```list```, ```set```
        
</details>

<details>
<summary> 2. Функциональное программирование </summary>

   - ```lambda```, ```zip```, ```map```, ```filter```, ```reduce``` (functools)

   ``` python
   numbers = range(10)
   squared_evens = map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers))
   list(squared_evens)   # [0, 4, 16, 36, 64]
   ```

   - декораторы:
   
   ``` python
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
<summary>  </summary>
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

