function videoController($scope, $http, $routeParams, $sce) {
    console.log($routeParams);
    $http.get('/api/v1/charity_full?format=json').success(function(data) {
        $scope.items = data.append;
        console.log(data);
        console.log(data.objects);
        $scope.all = data.objects;
        console.log($scope.all);
        console.log($scope.all[0].charity.giver);
        $scope.quantity = 3;
        $scope.fliersOnly = function() {
		$scope.searchText = "flying";
        };
        for(var i=0; i < $scope.all.length; i++) {
            $scope.all[i].trusted_url = $sce.trustAsResourceUrl($scope.all[i].video_url);
            console.log($scope.all[i].trusted_url);
            $scope.random = function() {
                return Math.random();
            };
            $scope.all[i].random_giver = $scope.all[i].charity.givers[Math.floor(Math.random() * $scope.all[i].charity.givers.length)];
        }
    });

        $scope.facebookLike = function() {
        $http.post('/api/v1/click_count/?format=json', $scope.objects).
            success(function(response){
                $location.path("/");
            })
    };

        $scope.facebookShare = function() {
        $http.post('/api/v1/click_count/?format=json', $scope.objects).
            success(function(response){
                $location.path("/");
            })
    };

        $scope.facebookSend = function() {
        $http.post('/api/v1/click_count/?format=json', $scope.objects).
            success(function(response){
                $location.path("/");
            })
    };

        $scope.section = function (id) {
            section = id;
    };

        $scope.is = function (id) {
            return section == id;
    };
}




