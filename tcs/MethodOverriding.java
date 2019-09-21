class Parent{
    void show(){
        System.out.println("I am from parent");
    }
}
class Child extends Parent{
    @Override
    void show(){
        System.out.println("I am from child");
    }
}
class MethodOverriding{
    public static void main(String args[]){
        Parent obj1 = new Parent();
        obj1.show();
        Parent obj2 = new Child();
        obj2.show();
    }
}