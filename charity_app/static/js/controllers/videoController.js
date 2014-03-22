function videoController($scope, $http, $routeParams, $sce) {
    console.log($routeParams);
    $http.get('/api/v1/charity_full/?format=json').success(function (data) {
        $scope.items = data.append;
        console.log(data);
        $scope.all = data.objects;
        $scope.quantity = 3;
        $scope.fliersOnly = function () {
            $scope.searchText = "flying";
        };

        for (var i = 0; i < $scope.all.length; i++) {
            $scope.all[i].trusted_url = $sce.trustAsResourceUrl($scope.all[i].video_url);
            console.log($scope.all[i].trusted_url);
            $scope.random = function () {
                return Math.random();
            };
            $scope.all[i].random_giver = $scope.all[i].charity.givers[Math.floor(Math.random() * $scope.all[i].charity.givers.length)];
        }
    });

    $scope.facebookLike = function (item) {
        $http.post('/api/v1/click_count/?format=json', {"facebook_count": "like", "video": item.resource_uri}).
            success(function (response) {
                console.log(response);
                $location.path("/");

            })
    };

    $scope.facebookShare = function (item) {
        $http.post('/api/v1/click_count/?format=json', {"facebook_count": "share", "video": item.resource_uri}).
            success(function (response) {
                console.log(response);
                $location.path("/");
            })
    };

    $scope.facebookSend = function (item) {
        $http.post('/api/v1/click_count/?format=json', {"facebook_count": "send", "video": item.resource_uri}).
            success(function (response) {
                console.log(response);
                $location.path("/");
            })
    };

    $scope.section = function (id) {
        $scope.section_id = id;
    };

    $scope.is = function (id) {
        return $scope.section_id == id;
    };

    $scope.slides = [
        'http://flexslider.woothemes.com/images/kitchen_adventurer_cheesecake_brownie.jpg',
        'http://flexslider.woothemes.com/images/kitchen_adventurer_lemon.jpg',
        'http://flexslider.woothemes.com/images/kitchen_adventurer_donut.jpg',
        'http://flexslider.woothemes.com/images/kitchen_adventurer_caramel.jpg'
    ];
}

