//copying the videolink

const copybtns = [...document.getElementsByClassName('copy-btn')]


copybtns.forEach(btn=>btn.addEventListener('click', ()=>{
    const vid_id = btn.getAttribute('vidId')
    const vid_link = `https://www.youtube.com/watch?v=${vid_id}`
    navigator.clipboard.writeText(vid_link)
    btn.textContent='Copied✔️'
}))