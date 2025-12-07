document.getElementById("addWineForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const res = await fetch("/add", { method: "POST", body: formData });
    if (res.ok) { alert("Wein hinzugefügt!"); window.location.reload(); }
    else { alert("Fehler"); }
});
