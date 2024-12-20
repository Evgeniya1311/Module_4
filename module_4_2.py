def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
#inner_function()  ошибка, т.к. данная ф-ия находится в локальном пространстве ф-ии test_function() и существует только внутри нее