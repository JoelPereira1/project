
const toggleSibebar = () => {
    const isCollapse = document.body.classList.contains('sidebar-collapse')
    const content = document.getElementById('content')
    content.classList.remove('no-transition')
    const header = document.getElementById('header')
    header.classList.remove('no-transition')
    if (isCollapse) {
        document.body.classList.remove('sidebar-collapse')
    } else {
        document.body.classList.add('sidebar-collapse')
    }
}
const toggleSidebarBtn = document.getElementById('toggleSidebar')
toggleSidebarBtn.addEventListener('click', toggleSibebar)

const toggleMenu = (menu) => {
    const sub = menu.getElementsByClassName('nav-treeview')[0]
    const isOpen = menu.classList.contains('menu-open')
    if (isOpen) {
        sub.style.display = 'none'
        menu.classList.remove('menu-open')
    } else {
        sub.style.display = 'block'
        menu.classList.add('menu-open')
    }

}
const toggleMenuBtns = document.querySelectorAll('.has-treeview')
toggleMenuBtns.forEach((menu) => {
    const callback = toggleMenu.bind(this, menu)
    menu.addEventListener('click', callback)
})

const deleteModal = document.getElementById('deleteModal')
deleteModal.addEventListener('show.bs.modal', event => {
    const triggerBtn = event.relatedTarget
    const deleteUrl = triggerBtn.dataset.deleteUrl
    const redirectUrl = triggerBtn.dataset.redirectUrl
    const confirmBtn = document.getElementById('confirmDelete')
    const deleteToast = document.getElementById('deleteToast')
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content')
    confirmBtn.addEventListener('click', () => {
        fetch(`/dashboard/${deleteUrl}`, {method: 'DELETE', headers: {'X-CSRF-Token': csrfToken}}).then(response => {
            if(response.ok){
                return response.json()
            }
            throw new Error('Network was not ok!')
        }).then(data => {
            if (data.code === 0) {
                const toast = new bootstrap.Toast(deleteToast)
                toast.show()
                const modal = bootstrap.Modal.getInstance(deleteModal);
                modal.hide()
                if (redirectUrl) {
                    setTimeout(function () {
                        window.location.replace(redirectUrl);
                    }, 1000)
                } else {
                    triggerBtn.closest('tr').remove();
                }
            } else {
                console.log(data)
            }
        })
    })
})

document.querySelectorAll('select').forEach((el) => {
    new TomSelect(el, {});
});

document.querySelectorAll('.msg-toast').forEach((el) => {
    const toast = new bootstrap.Toast(el)
    toast.show()
})