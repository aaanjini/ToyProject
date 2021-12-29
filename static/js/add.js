function addMusic(){
    $.ajax({
        type:'POST',
        url :'/add/music',
        data:{musicUrl: $('#music-url').val()},
        success: function (response){
            $('#music-box').empty();
            alert(response['msg']);
            showMusic(response['id']);
            //window.location.reload();
        }
    })
}


function showMusic(id){
    $.ajax({
        type:"GET",
        url:"/add/music/" + id,
        data:{},
        success: function(response){          
            let img_url = response['url'];
            let name = response['name'];
            let artist = response['artist'];
            let temp_html = `<div class="card">
                                <div class="card-content">
                                    <div class="media">
                                        <div class="media-left">
                                            <figure class="image is-48x48">
                                                <img
                                                        src=${img_url}
                                                        alt="Placeholder image"
                                                />
                                            </figure>
                                        </div>
                                        <div class="media-content">
                                            <a href="#" target="_blank" class="star-name title is-4">${artist}</a>
                                            <p class="subtitle is-6">${name}</p>
                                        </div>
                                    </div>
                                </div>
                                <footer class="card-footer">
                                </footer>
                            </div>`
            $('#music-box').append(temp_html);
        }
    }
)}
