/**
 * For use in Compsci 201, P0, Duke University
 * @author ola, Owen Astrachan
 * To be modified by students in 201, when you make
 * a modification, add yourself as an author in these
 * comments.
 * @version 3.0, Fall 2024, changed getters
 * to mirror record getters and phrase to eatery
 *
 */
public class Person201 {
    private String name;      // name of person
    private double latitude;  // N is +, S is -
    private double longitude; // W is -, E is +
    private String eatery;    // on ninth street

    public Person201(String name, double latitude, double longitude, String eatery) {
        this.name = name;
        this.latitude = latitude;
        this.longitude = longitude;
        this.eatery = eatery;
    }
    public Person201(){
        this("Owen", 35.99, 78.9, "Dain's Place");

    }

    // getters
    public String name(){
        return name;
    }
    public double latitude(){
        return latitude;
    }
    public double longitude(){
        return longitude;
    }
    public String eatery(){
        return eatery;
    }

    @Override
    public boolean equals(Object o){
        Person201 other = (Person201) o;
        return name().equals(other.name()) &&
               latitude() == other.latitude() &&
               longitude() == other.longitude() &&
               eatery().equals(other.eatery());
    }

    /**
     * Returns String using E/W for longitude, N/S for latitude
     */
    
    @Override
    public String toString(){
        String lats = String.format("%06.2f",Math.abs(latitude));
        if (latitude < 0) {
            lats += "S";
        }
        else {
            lats += "N";
        }
        String lons = String.format("%06.2f",Math.abs(longitude));
        if (longitude < 0) {
            lons += "W";
        }
        else {
            lons += "E";
        }
        return String.format("(%s,%s) %s, \"%s\"",lats,lons,name,eatery);
    }
    public static void main(String[] args) {
        Person201 p = new Person201("Owen",35.994, 78.898, "Dain's Place");
        System.out.println(p);
    }
}