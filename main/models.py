from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator
User = get_user_model()

class Category(models.Model):
    title= models.CharField(
        max_length=123,
        verbose_name='Название'
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Image(models.Model):
    file = models.ImageField(
        upload_to='media/product_file',
        verbose_name='Файл'
    )

    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продуктов'


class Product(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models. CharField(
        max_length=123,
        verbose_name='Название'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='Категория'
    )
    main_image = models.ImageField(
        upload_to='media/main_covers',
        verbose_name='Главное фото',
        help_text='Фото которое будет отображаться на обложке обьявления'
    )
    images = models.ManyToManyField(
        Image,
        verbose_name='Изображения'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Цена'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Rating(models.Model):
    user = models.ForeignKey(
         User,
         on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    count = models.PositiveSmallIntegerField(
         validators=[MinValueValidator(1), MaxLengthValidator(5)],
         verbose_name='Оценка'
    )
    comment = models.TextField(
        max_length=500,
        verbose_name='Коментарий'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return f'{self.user} -->{self.product}'


    class Meta:
         verbose_name = 'Отзыв'
         verbose_name_plural = 'Отзывы'


class RatingAnswer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    rating = models.ForeignKey(
        Rating,
        on_delete=models.CASCADE,
        verbose_name='Отзыв',
        related_name='rating_answers'
    )
    comment = models.TextField(
        max_length=500,
        verbose_name='Коментарий'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )
    time_limit = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Ограничение по времени'
    )

    def __str__(self):
        return f'{self.user} -->{self.rating}'
    class Meta:
         verbose_name = 'Ответ на отзыв'
         verbose_name_plural = 'Ответы на отзывы'



class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name='Оплачено'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество'
    )

    #def __str__(self):
        #return
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Закавы'
