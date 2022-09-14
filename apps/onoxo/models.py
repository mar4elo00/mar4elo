from django.db import models



class Tests(models.Model):
  
    """
    check
    """
    test1 = models.CharField(unique=True, verbose_name="name 1",max_length=255, null=True )
    test2 = models.CharField(verbose_name="name 2",max_length=255, null=True, blank=True )

    class Meta:
        verbose_name = "Test_Name"
        verbose_name_plural = "Test_Name"

    def __str__(self):
        return self.test1


   