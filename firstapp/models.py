from django.db import models


class Exterior(models.Model):
    description = models.CharField("Описание", max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Экстерьер"
        verbose_name_plural = "Экстерьеры"


class Character(models.Model):
    character = models.CharField("Описание", max_length=255)

    def __str__(self):
        return self.character

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"


class Vehicle(models.Model):
    name = models.CharField('Марка авто', max_length=255)
    description = models.TextField('Описание', max_length=5000)
    year = models.IntegerField('Год выпуск', default=2020)
    doors = models.IntegerField('Количество дверей')
    seats = models.IntegerField('Количество мест')
    lugage = models.CharField('Кузов', max_length=255)
    transmission = models.CharField('Трансмиссия', max_length=255)
    minimum_age = models.IntegerField('Возвраст')
    image = models.ImageField('Изображение', upload_to='vehicles/')
    slug = models.SlugField()
    exterior = models.ManyToManyField(Exterior, verbose_name='Экстерьеры')
    character = models.ManyToManyField(Character, verbose_name='Характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class VehicleShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="vehicle_shots/")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vehicle.name}-{self.title}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображение"


class Service(models.Model):
    name = models.CharField('Название сервиса', max_length=255)
    description = models.TextField('Описание', max_length=5000)
    image = models.ImageField('Изображение', upload_to='services/')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    image = models.ImageField('Изображение', upload_to='reviews/', blank=True)
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.surname} -{self.email}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Blog(models.Model):
    title = models.CharField("Титул", max_length=100)
    data = models.DateField('Дата')
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='blog/')
    slug = models.SlugField()

    def __str__(self):
        return f"{self.title} - {self.data}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"
