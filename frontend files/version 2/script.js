function toggleTheme() {
    document.body.classList.toggle('darkmode');
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const body = document.body;

    if (sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
        body.classList.remove('sidebar-open');
    } else {
        sidebar.classList.add('open');
        body.classList.add('sidebar-open');
    }
}


const apiKey = "pub_55255090e1ecf39c3c34382da2160920752a2"; // Replace with your actual API key

const fetchData = async (category) => {
// Check if data is already stored in localStorage
const cachedData = localStorage.getItem(category);

if (cachedData) {
    // If data is available in localStorage, return it
    console.log("Using cached data");
    return JSON.parse(cachedData);
}

const url = `https://newsdata.io/api/1/news?apikey=${apiKey}&country=in&category=${category}&language=en`;
try {
    const response = await fetch(url);
    const data = await response.json();

    // Store the fetched data in localStorage
    localStorage.setItem(category, JSON.stringify(data.results));

    return data.results;
} catch (error) {
    console.error("Error fetching data:", error);
    return [];
}
};


// Fetch Top News
const add_topNews = (data) => {
let html = '';
data.forEach((newsItem) => {
    let title = newsItem.title.length < 100 ? newsItem.title : newsItem.title.slice(0, 100) + '...';
    html +=`<div class="article-card " >
        <img src="${newsItem.image_url}" alt="Article Image" class="article-image">
        <div class="article-details">
            <h3 class="${title}">Breaking News: Important Update</h3>
            <p class="article-summary">This is a brief summary of the breaking news article. More details inside...</p>
            <a href="${newsItem.link}" class="read-more">Read more</a>
        </div>
    </div>`
});
topNews.innerHTML = html;
};
fetchData('top').then(add_topNews);


const add_entertainmentNews = (data) => {
let html = '';
data.forEach((newsItem) => {
    let title = newsItem.title.length < 100 ? newsItem.title : newsItem.title.slice(0, 100) + '...';
    html +=`<div class="article-card " >
        <img src="${newsItem.image_url}" alt="Article Image" class="article-image">
        <div class="article-details">
            <h3 class="${title}">Breaking News: Important Update</h3>
            <p class="article-summary">This is a brief summary of the breaking news article. More details inside...</p>
            <a href="${newsItem.link}" class="read-more">Read more</a>
        </div>
    </div>`
});
topNews.innerHTML = html;
};
fetchData('entertainment').then(add_entertainmentNews);


const add_worldNews = (data) => {
let html = '';
data.forEach((newsItem) => {
    let title = newsItem.title.length < 100 ? newsItem.title : newsItem.title.slice(0, 100) + '...';
    html +=`<div class="article-card " >
        <img src="${newsItem.image_url}" alt="Article Image" class="article-image">
        <div class="article-details">
            <h3 class="${title}">Breaking News: Important Update</h3>
            <p class="article-summary">This is a brief summary of the breaking news article. More details inside...</p>
            <a href="${newsItem.link}" class="read-more">Read more</a>
        </div>
    </div>`
});
topNews.innerHTML = html;
};
fetchData('world').then(add_worldNews);


// const add_topNews = (data) => {
// let html = '';
// data.forEach((newsItem) => {
//     let title = newsItem.title.length < 100 ? newsItem.title : newsItem.title.slice(0, 100) + '...';
//     html +=`<div class="article-card " >
//         <img src="${newsItem.image_url}" alt="Article Image" class="article-image">
//         <div class="article-details">
//             <h3 class="${title}">Breaking News: Important Update</h3>
//             <p class="article-summary">This is a brief summary of the breaking news article. More details inside...</p>
//             <a href="${newsItem.link}" class="read-more">Read more</a>
//         </div>
//     </div>`
// });
// topNews.innerHTML = html;
// };
// fetchData('top').then(add_topNews);
// const add_topNews = (data) => {
// let html = '';
// data.forEach((newsItem) => {
//     let title = newsItem.title.length < 100 ? newsItem.title : newsItem.title.slice(0, 100) + '...';
//     html +=`<div class="article-card " >
//         <img src="${newsItem.image_url}" alt="Article Image" class="article-image">
//         <div class="article-details">
//             <h3 class="${title}">Breaking News: Important Update</h3>
//             <p class="article-summary">This is a brief summary of the breaking news article. More details inside...</p>
//             <a href="${newsItem.link}" class="read-more">Read more</a>
//         </div>
//     </div>`
// });
// topNews.innerHTML = html;
// };
// fetchData('top').then(add_topNews);
// const add_topNews = (data) => {
// let html = '';
// data.forEach((newsItem) => {
//     let title = newsItem.title.length < 100 ? newsItem.title : newsItem.title.slice(0, 100) + '...';
//     html +=`<div class="article-card " >
//         <img src="${newsItem.image_url}" alt="Article Image" class="article-image">
//         <div class="article-details">
//             <h3 class="${title}">Breaking News: Important Update</h3>
//             <p class="article-summary">This is a brief summary of the breaking news article. More details inside...</p>
//             <a href="${newsItem.link}" class="read-more">Read more</a>
//         </div>
//     </div>`
// });
// topNews.innerHTML = html;
// };
// fetchData('top').then(add_topNews);


 function changeContent(category) {
		// Update the section title and the ID of the main content
		const sectionTitle = document.querySelector(".section-title");
		const mainContent = document.querySelector(".articles");

		sectionTitle.textContent = category; 
        let result = category.replace(/\s+/g, ""); // Remove all spaces
		result = result.charAt(0).toLowerCase() + result.slice(1);// Change title
		mainContent.id = result; // Change ID dynamically

		// Optionally, you can add specific content depending on the category
		// Here we are just setting a simple message
		const articlesDiv = mainContent.querySelector(".articles");
		articlesDiv.innerHTML = `<p>Displaying ${category} content...</p>`;
 }