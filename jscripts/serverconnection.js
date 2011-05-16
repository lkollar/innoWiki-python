function ServerConnection(){
    this.siteUrl = "http://localhost:8888";
	this.historyList = "innowiki-history";

    // TODO
	this.getPageFromHistory = function (title){
    }

    // TODO
	this.getLastHistoryId = function(){
    }

    // TODO
	this.getActivePage = function(title){
    }

    // TODO
	this.getActivePageList = function (){
    }

    // TODO
	this.getPagesFromHistoryNewerThan = function (id){
    }

    // TODO
	this.getCurrentUserLogin = function (){
        return "FooBar";
    }

    // TODO
    // We probably don't need this.
	this.getUserlist = function (){
            /*
            $.getJSON(this.siteUrl+ "/_userlist", function(data) {
                        user = new innoWiki.classes.UserItem(
                            data["ID"],
                            data["Name"],
                            data["LoginName"],
                            data["Email"])

                        return user;
                    });

            */
    }



	// private
    // TODO
	this.getItems =	function (listName, queryString, viewFields, rowLimit){
				
    }

    // TODO
	this.save = function (page){
    }

    // TODO
	this.handleErrors = function(response){
    }
}
