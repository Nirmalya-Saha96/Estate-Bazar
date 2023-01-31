function scrapper() {
    fetch("/admin", {
      method: "POST"
    }).then((_res) => {
      window.location.href = "/admin";
    });
}

function activateAuction(propertyId) {
  fetch("/admin", {
    method: "PUT",
    body: JSON.stringify({ propertyId: propertyId })
  }).then((_res) => {
    window.location.href = "/admin";
  });
}

function deleteAuction(propertyId) {
  fetch("/admin", {
    method: "DELETE",
    body: JSON.stringify({ propertyId: propertyId })
  }).then((_res) => {
    window.location.href = "/admin";
  });
}

function deActivateAuction(propertyId) {
  fetch("/admin/active-auctions", {
    method: "PUT",
    body: JSON.stringify({ propertyId: propertyId })
  }).then((_res) => {
    window.location.href = "/admin/active-auctions";
  });
}
  