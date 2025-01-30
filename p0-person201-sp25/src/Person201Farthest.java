public class Person201Farthest {
    public static void main(String[] args) throws Exception{
        String file = "data/foodlarge.txt";
        double max = 0;
        Person201 a = null;
        Person201 b = null;

        Person201[] people = Person201Utilities.readFile(file);

        //Iteration
        for (int i = 0; i<people.length;i++) {
            for(int j = i+1; j<people.length ;j++){

                double d = Person201Utilities.distance(people[i],people[j]);
                //Comparison
                if(d>=max){
                    max = d;
                    a = people[i];
                    b = people[j];
                }
            }
            
        }
        
        System.out.printf("farthest distance is %3.2f between %s and %s\n",max,a.name(),b.name());
    }
}
