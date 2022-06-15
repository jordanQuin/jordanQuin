package eraser;

public class Eraser {
    /**
     * Retourne une chaîne de caractères dont on a enlevé les espaces qui sont par un (s'il y a une suite de deux ou plus espaces, ils sont gardés)
     * 
     * @param str la chaîne de caractères à "nettoyer"
     * 
     * @return la chaîne de caractères nettoyée
     */
    public static String erase(String str) {
        String str_erased = ""; // Initialisation du nouveau String
        int size = str.length();
        for(int i = 0; i < size; i++) {
            // On vérifie si le caractère à l'emplacement i est un espace
            if(str.charAt(i) == ' ') { 
                // Si c'est le cas, on va chercher à récupérer la suite d'espaces s'il y en a une 
                int compteur = 1;
                while(i+compteur < size && str.charAt(i+compteur) == ' ') {
                    // On continue de parcourir le String en vérifiant de ne pas dépasser, tant que le caractère suivant est un espace
                    str_erased += ' '; // On ajoute un espace au String à retourner
                    compteur++; // On compte le nombre d'espaces trouvés
                }
                // On vérifie si on a trouvé au moins un autre espace suivant
                if(compteur != 1) {
                    // Il y a eu au moins un autre espace suivant, on ajoute donc l'espace correspondant au premier trouvé à i
                    str_erased += ' ';
                    // On incrémente i de compteur - 1 afin de "sauter" les étapes qui consisteraient à tester chaque espace un par un
                    // On avance ainsi jusqu'au prochain caractère différent d'un espace.
                    i+=compteur-1;
                }
                // On ne fait rien si on n'a pas trouvé d'espace suivant : il n'y a qu'un donc on souhaite l'enlever
            }else {
                // On ne traite pas un espace, on ajoute donc le caractère normalement
                str_erased += str.charAt(i);
            }
        }
        return str_erased;
    }
}
