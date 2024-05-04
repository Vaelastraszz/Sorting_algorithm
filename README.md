URL de l'app : https://vaelastraszz-sorting-algorithm-sorting-algorithms-7aawuz.streamlit.app/

Script pour visualiser trois différents types d'algorithme de sorting : 
- Bubble Sort :
Le tri à bulles ou tri par propagation1 est un algorithme de tri. Il consiste à comparer répétitivement les éléments consécutifs d'un tableau, et à les permuter lorsqu'ils sont mal triés. Il doit son nom au fait qu'il déplace rapidement les plus grands éléments en fin de tableau, comme des bulles d'air qui remonteraient rapidement à la surface d'un liquide.
Le tri à bulles est souvent enseigné en tant qu'exemple algorithmique, car son principe est simple. Mais c'est le plus lent des algorithmes de tri communément enseignés, et il n'est donc guère utilisé en pratique.

![Sorting_bubblesort_anim](https://github.com/Vaelastraszz/Sorting_algorithm/assets/47340421/e0b7c4d4-195c-4bbc-aceb-ac4fe1011963)

Le Quick Sort : 
En informatique, le tri rapide ou tri pivot (en anglais quicksort) est un algorithme de tri inventé par C.A.R. Hoare en 19613 et fondé sur la méthode de conception diviser pour régner. Il est généralement utilisé sur des tableaux, mais peut aussi être adapté aux listes. Dans le cas des tableaux, c'est un tri en place mais non stable.

La complexité moyenne du tri rapide pour n éléments est proportionnelle à n log n, ce qui est optimal pour un tri par comparaison, mais la complexité dans le pire des cas est quadratique. Malgré ce désavantage théorique, c'est en pratique un des tris les plus rapides, et donc un des plus utilisés. Le pire des cas est en effet peu probable lorsque l'algorithme est correctement mis en œuvre et il est possible de s'en prémunir définitivement avec la variante Introsort.

Le tri rapide ne peut cependant pas tirer avantage du fait que l'entrée est déjà presque triée. Dans ce cas particulier, il est plus avantageux d'utiliser le tri par insertion ou l'algorithme smoothsort.

![Sorting_quicksort_anim](https://github.com/Vaelastraszz/Sorting_algorithm/assets/47340421/581a6714-a3a7-499e-95e7-bfeb19f3d440)

L'Insert Sort :
En informatique, le tri par insertion est un algorithme de tri classique. La plupart des personnes l'utilisent naturellement pour trier des cartes à jouer1.

En général, le tri par insertion est beaucoup plus lent que d'autres algorithmes comme le tri rapide (ou quicksort) et le tri fusion pour traiter de grandes séquences, car sa complexité asymptotique est quadratique.

Le tri par insertion est cependant considéré comme l'algorithme le plus efficace sur des entrées de petite taille. Il est aussi efficace lorsque les données sont déjà presque triées. Pour ces raisons, il est utilisé en pratique en combinaison avec d'autres méthodes comme le tri rapide.

En programmation informatique, on applique le plus souvent ce tri à des tableaux. La description et l'étude de l'algorithme qui suivent se restreignent à cette version, tandis que l'adaptation à des listes est considérée plus loin.

![Insertion_sort_animation](https://github.com/Vaelastraszz/Sorting_algorithm/assets/47340421/d9f9e563-3a4f-4c1e-9a84-78d7fc34487b)
