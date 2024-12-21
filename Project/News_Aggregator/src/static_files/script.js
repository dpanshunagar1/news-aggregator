function toggleTheme() {
	document.body.classList.toggle("darkmode");
}

function toggleSidebar() {
	const sidebar = document.getElementById("sidebar");
	const body = document.body;

	if (sidebar.classList.contains("open")) {
		sidebar.classList.remove("open");
		body.classList.remove("sidebar-open");
	} else {
		sidebar.classList.add("open");
		body.classList.add("sidebar-open");
	}
}

function loadCategory(category) {
	// Make an AJAX request to fetch articles for the selected category
	fetch(`/category/${category}/`)
		.then((response) => response.text()) // Get the HTML content from the server
		.then((data) => {
			// Update the content of the main section dynamically
			document.querySelector(".main-content").innerHTML = data;
		})
		.catch((error) => {
			console.error("Error loading category:", error);
		});
}

function changeContent(category) {
	// Update the section title and the ID of the main content
	const sectionTitle = document.querySelector(".section-title");
	const mainContent = document.querySelector(".articles");

	sectionTitle.textContent = category;
	let result = category.replace(/\s+/g, ""); // Remove all spaces
	result = result.charAt(0).toLowerCase() + result.slice(1); // Change title
	mainContent.id = result; // Change ID dynamically

	// Optionally, you can add specific content depending on the category
	// Here we are just setting a simple message
	const articlesDiv = mainContent.querySelector(".articles");
	articlesDiv.innerHTML = `<p>Displaying ${category} content...</p>`;
}
