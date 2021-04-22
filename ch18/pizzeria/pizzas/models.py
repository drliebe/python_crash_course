from django.db import models

class Pizza(models.Model):
    """An individual pizza."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string represenation of the pizza."""
        if len(self.name) < 50:
            return self.name
        else:
            return self.name[:50] + "..."

class Topping(models.Model):
    """An individual topping."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return a string represenation of the topping."""
        if len(self.name) < 50:
            return self.name
        else:
            return self.name[:50] + "..."