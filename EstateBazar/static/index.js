function scrapper() {
    fetch("/admin", {
      method: "POST"
    }).then((_res) => {
      window.location.href = "/admin";
    });
  }
  