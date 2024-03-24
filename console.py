#!/usr/bin/python3

"""This module is for the console of the project"""

import cmd
from models.base_model import BaseModel
from models import storage


_classes = {
    "BaseModel": BaseModel
    }


class HBNBCommand(cmd.Cmd):
    """This class contains the console for the python cmd"""

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def do_create(self, arg):
        """
    Creates a new instance of a class, saves it to the storage,
    and prints its ID. If the class name is missing or doesn't
    exist, appropriate error messages are printed.
    """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in _classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{class_name}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
            Prints the string representation of an instance based on
            the class name and ID. If either the class name, instance ID,
            or the instance itself is missing, appropriate error messages
            are printed.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in _classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and ID, and saves
    the changes to the storage. If either the class name, instance ID,
    or the instance itself is missing, appropriate error messages
    are printed.
    """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in _classes:
            print("** class doesn't exist **")
            return

        key = f"{args[0]}.{args[1]}"
        obj = storage.all

        if key not in obj:
            print("** no instance found **")
            return
        else:
            del obj[key]
            storage.save()

    def do_all(self, arg):
        """
    Prints the string representation of all instances based on
    the class name. If the class name doesn't exist, all instances
    from all classes are printed. If the class name is missing, all
    instances from all classes are printed. If no instances are found,
    an appropriate error message is printed.
    """
        list_of_string = []
        obj = storage.all()
        args = arg.split()

        if not arg:
            for obj_key in obj.value():
                list_of_string.append(str(obj_key))
        else:
            class_name = args[0]
            if class_name not in _classes:
                print("** class doesn't exist **")
                return
            else:
                for obj_key in obj:
                    if obj[obj_key].__class__.__name__ == class_name:
                        list_of_string.append(str(obj[obj_key]))

        print(list_of_string)

    def do_update(self, arg):
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in _classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        else:
            if not args[2]:
                print("** attribute name missing **")
            elif args[2] and not args[3]:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3].replace('"', '')

                setattr(storage.all()[key], attr_name, attr_value)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
