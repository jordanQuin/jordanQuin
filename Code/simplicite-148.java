package main.java.eraser; 

public class Eraser { 
	public static String erase(String str) {     
		String soluce = ""; 
		int size = str.length(); //taille à parcourir
		for (int i = 0;i<size;i++) {     
			if (str.charAt(i)==32) { //recherche d'un espace        
				if ((i+1<size&&str.charAt(i+1)==32)|| ((i!=0&&str.charAt(i-1)==32))){ //recherche d'un second espace avant ou après          
					soluce+=str.charAt(i);
				}     
			}else {         
				soluce+=str.charAt(i);
			} 
		} System.out.println(soluce);        
		return soluce; 
	}
}
