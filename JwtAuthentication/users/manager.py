from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password = None, password2=None, first_name= None, last_name=None, role = None):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('Users must have an email address.')
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            role = role,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password, first_name, last_name, password2 =None, role = 0):
        """
        Creates and saves a superuser with the given email and password.
        """

        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)
        return user
    
    def create_admin(self, email, password, first_name, last_name, role =None):
        """
        Creates and saves a admin with the given email and password.
        """

        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role
        )
        user.save(using=self._db)
        return user