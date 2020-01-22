var instance = M.Tabs.init(document.getElementById('auth-tab-swipe'), {
    duration: 300
});

document.getElementById('login_tab').addEventListener('click', () => {
    instance.select('swipe-login')
    document.getElementById('login_tab').classList.add('tab_active')
    document.getElementById('signup_tab').classList.remove('tab_active')
})

document.getElementById('signup_tab').addEventListener('click', () => {
    instance.select('swipe-signup')
    document.getElementById('signup_tab').classList.add('tab_active')
    document.getElementById('login_tab').classList.remove('tab_active')
})