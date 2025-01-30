
/**
 * Demonstrate Reading Person201 objects and
 * determining distance values 
 */

public class Person201Nearby {
    public static void main(String[] args) throws Exception {
        Person201 query = new Person201("Ricardo",46.9994, -122.3921,"Juju");

        String largeFileName = "../data/foodlarge.txt";
        String smallFileName = "../data/foodsmall.txt";
        String largeURL = "https://courses.cs.duke.edu/fall24/compsci201/data/foodlarge.txt";
        Person201[] people = Person201Utilities.readURL(largeURL);

        System.out.println("distance\tperson");
        int total = 0;
        int threshold = 17;
        for (Person201 p : people) {
            double d = Person201Utilities.distance(query, p);   
            if (d < threshold) {
                System.out.printf("%3.2f:\t%s\n",d,p);
                total++;
            }
        }
        System.out.println("\nFound " + total + " people near " + query.name() + "\n");
    }
}
