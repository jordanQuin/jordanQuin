
public class Erase1 {

	public static String erase2 (String chaine) {

		char [] tab = chaine.toCharArray();
	    String res = "";
	    String var = "";
	    int cpt = 0;
	    int i;
	    
	    for (i=0; i<tab.length; i++) {
	    	if (tab [i] == ' ') {
	    		var += " ";
	    		cpt += 1;
	    	} else {
	    		if (cpt > 1)
	    			res += var;
	    		cpt = 0;
	    		var = "";
	    		res += tab [i];
	    	}
	    }

    	if (cpt > 1)
    		res += var;
	    
	    return res;
	    
	}
	
}
