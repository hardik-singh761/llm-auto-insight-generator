function uploadDataset() {
  let file = document.getElementById("fileInput").files[0];

  let formData = new FormData();

  formData.append("file", file);

  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then((res) => res.json())
    .then((data) => {
      let div = document.getElementById("results");

      div.innerHTML = "";

      data.forEach((item) => {
        let card = document.createElement("div");
        card.className = "card";

        let title = document.createElement("h3");
        title.innerText = item.column;

        let type = document.createElement("p");
        type.innerHTML = "<b>Chart Type:</b> " + item.chart_type;

        let img = document.createElement("img");
        img.src = "/charts/" + item.chart;

        let insight = document.createElement("p");
        insight.innerText = item.insight;

        card.appendChild(title);
        card.appendChild(type);
        card.appendChild(img);
        card.appendChild(insight);

        div.appendChild(card);
      });
    });
}
