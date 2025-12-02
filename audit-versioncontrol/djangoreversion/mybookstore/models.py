
from django.db import models
from reversion import register

@register()
class Client(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=20, blank=True)
	address = models.TextField(blank=True)

	def __str__(self):
		return self.name

@register()
class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	isbn = models.CharField(max_length=13, unique=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	stock = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.title} by {self.author}"

@register()
class SellOrder(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sell_orders')
	created_at = models.DateTimeField(auto_now_add=True)
	total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

	def __str__(self):
		return f"Order #{self.id} for {self.client.name}"

@register()
class SellOrderItem(models.Model):
	order = models.ForeignKey(SellOrder, on_delete=models.CASCADE, related_name='items')
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	price = models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return f"{self.quantity} x {self.book.title}"

@register()
class BorrowRequest(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='borrow_requests')
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	requested_at = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)
	returned = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.client.name} requests {self.book.title}"

@register()
class BorrowedBook(models.Model):
	borrow_request = models.OneToOneField(BorrowRequest, on_delete=models.CASCADE, related_name='borrowed_book')
	borrowed_at = models.DateTimeField(auto_now_add=True)
	due_date = models.DateTimeField()
	returned_at = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return f"{self.borrow_request.book.title} borrowed by {self.borrow_request.client.name}"
