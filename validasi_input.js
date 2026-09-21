document.getElementById('regForm').addEventListener('submit', function(e) {
    let u = document.getElementById('username').value.trim();
    let p = document.getElementById('password').value;
    let n = document.getElementById('nama').value.trim();
    let t = document.getElementById('tgl_lahir').value;
    let a = document.getElementById('alamat').value.trim();
    let tl = document.getElementById('telpon').value.trim();
    let today = new Date().toISOString().split('T')[0];

    if (!u || u.length < 3) { alert("Username minimal 3 karakter!"); e.preventDefault(); return; }
    if (!p || p.length < 8) { alert("Password minimal 8 karakter!"); e.preventDefault(); return; }
    if (!n) { alert("Nama tidak boleh kosong!"); e.preventDefault(); return; }
    if (!t || t < today) { alert("Tanggal lahir tidak boleh kosong atau masa lalu (wajib >= hari ini)!"); e.preventDefault(); return; }
    if (!a) { alert("Alamat tidak boleh kosong!"); e.preventDefault(); return; }
    if (!tl || !tl.startsWith("62")) { alert("Nomor telpon wajib diisi dan berawalan '62'!"); e.preventDefault(); return; }
});