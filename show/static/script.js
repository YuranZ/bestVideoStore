$("document").ready(function () {
    let id;
    // console.log("hello world");
    $(".like").on("click", function () {
                                console.log("click!!!");
                                id = $(this).attr("id");
                                //console.log(id);
                                $.ajax("/hello/ajax/add_like/",
                                    {"data":{"id":id},
                                            "method":"get",
                                            "success":function (data) {
                                                //console.log(data);
                                                $("#" + id).html("Likes: " + data)
                                            }
                                    }
                                )
                            }
                    )
    $(".btn-outline-dark").click(function () {
                                let id = $(this).attr('id');
                                console.log('Id '+id);
                                let val = $("#textarea" + id).val();
                                console.log(val);
                                $.ajax("/hello/add_ajax_comment/",
                                        {"data":{"id":id,"val":val},
                                        "method":"get",
                                        "success":function(data) {
                                           data = $.parseJSON(data);
                                           console.log(data);
                                           let row = "<h5>"+val+"</h5> <h6>"+data['date']+"</h6><hr>";
                                           $("#comment" + id).append(row)
                                           }
                                         }
                                        )
                                    }
                       )

});