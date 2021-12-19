import React from 'react';
import { BrowserRouter as Router, Switch, Route,Link} from "react-router-dom";
import { Header } from '../components/header';
import { Main } from '../pages/main';
import { Footer } from '../pages/footer';
import { NavBar } from '../components/navBar';
import { ContentList } from '../pages/contentList';
import { Detail } from '../pages/detail';

export const LoggedInRouter = () => {
    return (
        <Router>
            <Header />
            {/* <Switch> */}
                {/* <Route path="/"> */}
                <div className="container w-full md:max-w-5xl mx-auto pt-20">
                    <div className="grid grid-cols-2 md:grid-cols-3">
                        <div className="col-span-2">
                            <ContentList />
                            {/* <Main /> */}
                        </div>
                        <div>
                            <NavBar />
                        </div>
                    </div>
                </div>
                {/* </Route> */}
                {/* <Route path="/detail"> */}
                    <Detail />
                {/* </Route> */}
            {/* </Switch> */}
            {/* <Footer /> */}
        </Router>
        
    );
}