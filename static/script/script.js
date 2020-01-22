
document.getElementById('logoutBtn').addEventListener('click', () => {
    window.location.pathname = '/auth/logout'
    console.log('Logout')
})

document.getElementById('loginBtn').addEventListener('click', () => {
    window.location.pathname = '/auth'
    console.log('Login')
})
